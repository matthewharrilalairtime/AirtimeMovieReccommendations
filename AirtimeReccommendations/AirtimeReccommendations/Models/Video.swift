//
//  Video.swift
//  AirtimeReccommendations
//
//  Created by Matthew Harrilal on 5/27/21.
//

import Foundation


struct Video: Decodable {
    let items: [Item]
}

struct Item: Decodable {
    let id: String
    let contentDetails: ContentDetails
}

struct ContentDetails: Decodable {
    let duration: String
}
