//
//  Endpoint.swift
//  AirtimeReccommendations
//
//  Created by Matthew Harrilal on 5/27/21.
//

import Foundation

struct Endpoint {

    var path: String
    var queryItems: [URLQueryItem] = []
    var host: String
}

extension Endpoint {

    var url: URL {
        var components = URLComponents()
        components.scheme = "https"
        components.host = host
        components.path = path
        components.queryItems = queryItems

        guard let url = components.url else {
            preconditionFailure("Invalid URL components: \(components)")
        }

        return url
    }
}
