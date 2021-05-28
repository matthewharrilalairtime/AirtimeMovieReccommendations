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

        let outputStream = OutputStream(toFileAtPath: "/Users/matthewharrilal/AirtimeMovieReccommendations/csv/youtube_reduced_indexed.csv", append: false)!
        let outputCSV = try! CSVWriter(stream: outputStream)

        while let row = csv.next() {
            let youtubeVideoId = row[3].components(separatedBy: "=")
            if youtubeVideoId.count == 1 {
                continue
            }

            videoIds.append(youtubeVideoId[1])
            count += 1


            outputCSV.beginNewRow()
            try! outputCSV.write(row: [row[0], row[1], row[2], row[3], row[4], youtubeVideoId[1]])
        }

        print(videoIds, count)
        outputCSV.stream.close()

    }
}

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}


