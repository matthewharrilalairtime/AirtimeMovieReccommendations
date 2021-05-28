//
//  VideoLogicController.swift
//  AirtimeReccommendations
//
//  Created by Matthew Harrilal on 5/27/21.
//

import Foundation
import Combine

protocol VideoLogicControllerProtocol: class {
    func getVideos(id: String) -> AnyPublisher<Video, Error>
}

final class VideoLogicController: VideoLogicControllerProtocol {

    let networkController: NetworkController

    init(networkController: NetworkController) {
        self.networkController = networkController
    }

    func getVideos(id: String) -> AnyPublisher<Video, Error> {
        let endpoint = Endpoint.videos(id: id)

        return networkController.get(type: Video.self, url: endpoint.url, headers: [
            "Accept": "application/json"
        ])
    }
}

