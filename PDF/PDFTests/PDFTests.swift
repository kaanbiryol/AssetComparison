//
//  PDFTests.swift
//  PDFTests
//
//  Created by Kaan Biryol on 11.08.22.
//

import XCTest
import SnapshotTesting
@testable import PDF

class PDFTests: XCTestCase {

    func test() {
        let colors: [UIColor] = [.red]
        let stackView = UIStackView()
        stackView.distribution = .fillEqually
        stackView.axis = .vertical
        
        let bundleBeingTested = Bundle(identifier: "biryol.PDF")!
        for i in 0...1172 {
            let image = UIImage(named: "\(i)asset", in: bundleBeingTested, compatibleWith: nil)
            let imageView = UIImageView(image: image)
            let innerStackView = UIStackView()
            innerStackView.spacing = 8
            innerStackView.axis = .horizontal
            for color in colors {
                imageView.tintColor = color
                let label = UILabel()
                label.text = "\(i)asset, color \(color.description)"
                innerStackView.addArrangedSubview(label)
                innerStackView.addArrangedSubview(imageView)
            }
            stackView.addArrangedSubview(innerStackView)
        }
        
        let size = stackView.systemLayoutSizeFitting(UIView.layoutFittingCompressedSize)
        stackView.frame = CGRect(origin: .zero, size: size)
        
        assertSnapshot(matching: stackView, as: .image)
    }

}
