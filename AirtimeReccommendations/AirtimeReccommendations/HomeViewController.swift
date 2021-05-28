//
//  ViewController.swift
//  AirtimeReccommendations
//
//  Created by Matthew Harrilal on 5/27/21.
//

import UIKit
import Foundation
import CSV

class HomeViewController: UIViewController {

    private var videoIds: [String] = []
    private var count = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        let stream = InputStream(fileAtPath: "/Users/matthewharrilal/AirtimeMovieReccommendations/csv/youtube_reduced_indexed.csv")!
        let csv = try! CSVReader(stream: stream)
        while let row = csv.next() {
            let youtubeVideoId = row[3].components(separatedBy: "=")
            if youtubeVideoId.count == 1 {
                continue
            }

            videoIds.append(youtubeVideoId[1])
            count += 1

            let stream = OutputStream(toFileAtPath: "/Users/matthewharrilal/AirtimeMovieReccommendations/csv/youtube_reduced_indexed.csv", append: false)!
            let csv = try! CSVWriter(stream: stream)

            csv.beginNewRow()
            try! csv.write(field: youtubeVideoId[1])
            csv.stream.close()

            if count > 100 {
                break
            }
        }

        print(videoIds, count)
    }
}

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}


