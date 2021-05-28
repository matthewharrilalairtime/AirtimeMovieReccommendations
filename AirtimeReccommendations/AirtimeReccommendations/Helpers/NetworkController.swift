//
//  NetworkController.swift
//  AirtimeReccommendations
//
//  Created by Matthew Harrilal on 5/27/21.
//

import Foundation
import Combine

protocol NetworkControllerProtocol: class {
    typealias Headers = [String: Any]

    // Pass in a model of varying types and return a publisher that can send that model and a completion event downstream
    func get<T>(type: T.Type, url: URL, headers: Headers?) -> AnyPublisher<T, Error> where T: Decodable
}

final class NetworkController: NetworkControllerProtocol {

    func get<T>(type: T.Type, url: URL, headers: Headers?) -> AnyPublisher<T, Error> where T : Decodable {

        var urlRequest = URLRequest(url: url)

        headers?.forEach { (key, value) in
            if let value = value as? String {
                urlRequest.setValue(value, forHTTPHeaderField: key)
            }
        }

        return URLSession.shared.dataTaskPublisher(for: urlRequest)
            .map(\.data)
            .decode(type: T.self, decoder: JSONDecoder())
            .eraseToAnyPublisher()
    }
}

