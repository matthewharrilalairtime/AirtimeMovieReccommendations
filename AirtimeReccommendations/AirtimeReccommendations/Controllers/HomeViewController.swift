//
//  ViewController.swift
//  AirtimeReccommendations
//
//  Created by Matthew Harrilal on 5/27/21.
//

import UIKit
import Foundation
import Combine
import CSV

class HomeViewController: UIViewController {

    private var videoIds: [String] = []
    private var count = 0

    private var networkController = NetworkController()
    private lazy var videoLogicController = VideoLogicController(networkController: networkController)
    private var subscriptions = Set<AnyCancellable>()

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        populateVideoIds()
    }

    func writeToCSV(video: Video) {
        let stream = InputStream(fileAtPath: "/Users/matthewharrilal/AirtimeMovieReccommendations/csv/youtube_reduced_indexed.csv")!
        let csv = try! CSVReader(stream: stream)

        let outputStream = OutputStream(toFileAtPath: "/Users/matthewharrilal/AirtimeMovieReccommendations/csv/youtube_reduced_indexed.csv", append: false)!
        let outputCSV = try! CSVWriter(stream: outputStream)

        while let row = csv.next() {
            if row.count < 4 {
                continue
            }

            let youtubeVideoId = row[3].components(separatedBy: "=")
            if youtubeVideoId.count == 1 {
                continue
            }

            videoIds.append(youtubeVideoId[1])
            count += 1


            outputCSV.beginNewRow()

            let split = video.items[0].contentDetails.duration.components(separatedBy: "M")
            let minutes = split[0][split.count]
            let seconds = split[1][0]
            let duration = Int(row[4]) ?? 600 / ((minutes.wholeNumberValue! * 60) + seconds.wholeNumberValue!)
            try! outputCSV.write(row: [row[0], row[1], row[2], row[3], row[4], String(duration)])
        }

        print(videoIds, count)
        outputCSV.stream.close()
    }

    func populateVideoIds() {
        let stream = InputStream(fileAtPath: "/Users/matthewharrilal/AirtimeMovieReccommendations/csv/youtube_reduced_indexed.csv")!
        let csv = try! CSVReader(stream: stream)

        while let row = csv.next() {
            let youtubeVideoId = row[3].components(separatedBy: "=")
            if youtubeVideoId.count == 1 {
                continue
            }

            videoIds.append(youtubeVideoId[1])
        }

        print(videoIds, count)
        fetchVideos()
    }

    func fetchVideos() {
        videoIds.forEach { videoId in
            let semaphore = DispatchSemaphore(value: 0)
            videoLogicController.getVideos(id: videoId)
                .compactMap { $0 }
                .sink(receiveCompletion: { completion in
                    switch completion {
                    case .failure(let error):
                        print(error)
                    case .finished:
                        print("Finished")
                    }
                }, receiveValue: { [weak self] video in
                    semaphore.signal()
                    guard let self = self else { return }
                    self.writeToCSV(video: video)
                })
                .store(in: &subscriptions)

            _ = semaphore.wait(timeout: .distantFuture)
        }
    }
}

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}
