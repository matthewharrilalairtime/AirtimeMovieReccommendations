//
//  Endpoints.swift
//  AirtimeReccommendations
//
//  Created by Matthew Harrilal on 5/27/21.
//

import Foundation

extension Endpoint {

    static func videos(id: String) -> Self {
        return Endpoint(path: "/youtube/v3/videos", queryItems: [
            URLQueryItem(name: "part", value: "contentDetails"),
            URLQueryItem(name: "id", value: "\(id)"),
            URLQueryItem(name: "key", value: "\(youtubeAPIKey)")
        ], host: "youtube.googleapis.com")
    }
}
