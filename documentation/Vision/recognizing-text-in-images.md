# Recognizing Text in Images

**Framework**: Vision

Add text-recognition features to your app using the Vision framework.

#### Overview

One of Vision’s many powerful features is its ability to detect and recognize multilanguage text in images. You can use this functionality in your own apps to handle both real-time and offline use cases. In all cases, all of Vision’s processing happens on the user’s device to enhance performance and user privacy.

Vision’s text-recognition capabilities operate using one of these paths:

For example code using the fast path, see [`Extracting phone numbers from text in images`](extracting-phone-numbers-from-text-in-images.md).

For example code using the accurate path, see [`Structuring Recognized Text on a Document`](https://developer.apple.com/documentation/visionkit/structuring_recognized_text_on_a_document).

Using either path, you may optionally apply a language-correction phase based on Natural Language Processing (NLP) to minimize the potential for misreadings.

![An illustration contrasting the Vision framework’s fast text-recognition path with its accurate text-recognition path. ](https://docs-assets.developer.apple.com/published/f79b11e3d4a11c918935c5267ed1999e/media-3616311%402x.png)

> **Note**:  Using Vision’s text-recognition features is similar to performing other Vision operations, where you perform computer vision requests on an image and retrieve the resulting observations. If you’re new to the Vision framework, see [`Detecting Objects in Still Images`](detecting-objects-in-still-images.md).

 Using Vision’s text-recognition features is similar to performing other Vision operations, where you perform computer vision requests on an image and retrieve the resulting observations. If you’re new to the Vision framework, see [`Detecting Objects in Still Images`](detecting-objects-in-still-images.md).

##### Perform a Text Recognition Request

Vision provides its text-recognition capabilities through [`VNRecognizeTextRequest`](vnrecognizetextrequest.md), an image-based request type that finds and extracts text in images. The following example shows how to use [`VNImageRequestHandler`](vnimagerequesthandler.md) to perform a [`VNRecognizeTextRequest`](vnrecognizetextrequest.md) for recognizing text in the specified [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage).

```swift
// Get the CGImage on which to perform requests.
guard let cgImage = UIImage(named: "snapshot")?.cgImage else { return }

// Create a new image-request handler.
let requestHandler = VNImageRequestHandler(cgImage: cgImage)

// Create a new request to recognize text.
let request = VNRecognizeTextRequest(completionHandler: recognizeTextHandler)

do {
    // Perform the text-recognition request.
    try requestHandler.perform([request])
} catch {
    print("Unable to perform the requests: \(error).")
}
```

> **Note**:  [`VNRecognizeTextRequest`](vnrecognizetextrequest.md) uses the accurate path by default. To select the fast path, set the request’s [`recognitionLevel`](vnrecognizetextrequest/recognitionlevel.md) property to [`VNRequestTextRecognitionLevel.fast`](vnrequesttextrecognitionlevel/fast.md).

 [`VNRecognizeTextRequest`](vnrecognizetextrequest.md) uses the accurate path by default. To select the fast path, set the request’s [`recognitionLevel`](vnrecognizetextrequest/recognitionlevel.md) property to [`VNRequestTextRecognitionLevel.fast`](vnrequesttextrecognitionlevel/fast.md).

##### Process the Results

After the request handler processes the request, it calls the request’s completion closure, passing it the request and any errors that occurred. Retrieve the observations by querying the request object for its [`results`](vnrequest/results.md), which it returns as an array of [`VNRecognizedTextObservation`](vnrecognizedtextobservation.md) objects. Each observation provides the recognized text string, along with a confidence score that indicates the confidence in the accuracy of the recognition.

```swift
func recognizeTextHandler(request: VNRequest, error: Error?) {
    guard let observations =
            request.results as? [VNRecognizedTextObservation] else {
        return
    }
    let recognizedStrings = observations.compactMap { observation in
        // Return the string of the top VNRecognizedText instance.
        return observation.topCandidates(1).first?.string
    }
    
    // Process the recognized strings.
    processResults(recognizedStrings)
}
```

If you’d like to render the bounding rectangles around recognized text in your user interface, you can also retrieve that information from the observation. The rectangles it provides are in normalized coordinates. To render them correctly in your user interface, convert [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) instances from normalized coordinates to image coordinates by using the [`VNImageRectForNormalizedRect(_:_:_:)`](vnimagerectfornormalizedrect(_:_:_:).md) function as shown below.

```swift
let boundingRects: [CGRect] = observations.compactMap { observation in

    // Find the top observation.
    guard let candidate = observation.topCandidates(1).first else { return .zero }
    
    // Find the bounding-box observation for the string range.
    let stringRange = candidate.string.startIndex..<candidate.string.endIndex
    let boxObservation = try? candidate.boundingBox(for: stringRange)
    
    // Get the normalized CGRect value.
    let boundingBox = boxObservation?.boundingBox ?? .zero
    
    // Convert the rectangle from normalized coordinates to image coordinates.
    return VNImageRectForNormalizedRect(boundingBox,
                                        Int(image.size.width),
                                        Int(image.size.height))
}
```

The resulting bounding box differs depending on the path you choose. The fast path calculates the recognized text’s bounding rectangle based on its individual characters. The accurate path tokenizes on whitespace, which means when working with Chinese text, the resulting bounding boxes will likely contain lines or line fragments instead of complete text.

##### Optimize Language Settings

Your choice of fast or accurate path, along with your use of a particular API revision, determines the language support the text-recognition algorithms provide. To determine which languages a particular path and revision support, call the request’s [`supportedRecognitionLanguages(for:revision:)`](vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:).md) class method.

If not otherwise specified, Vision biases its results toward English. To alter its default behavior, provide an array of supported languages in the request’s [`recognitionLanguages`](vnrecognizetextrequest/recognitionlanguages.md) property. The order in which you provide the languages dictates their relative importance. To recognize traditional and simplified Chinese, specify `zh-Hant` and `zh-Hans` as the first elements in the request’s [`recognitionLanguages`](vnrecognizetextrequest/recognitionlanguages.md) property. English is the only other language that you can pair with Chinese.

Enabling language correction on the request helps minimize common recognition errors. If the text you’re recognizing uses domain-specific jargon, such as medical or technical terms, you can tailor the language correction’s behavior by setting the request’s [`customWords`](vnrecognizetextrequest/customwords.md) property. Language correction gives precedence to the custom words when performing its processing. The request ignores the [`customWords`](vnrecognizetextrequest/customwords.md) property if language correction isn’t enabled.

> **Note**:  Vision doesn’t support language correction, or its related [`customWords`](vnrecognizetextrequest/customwords.md) array, for Chinese.

 Vision doesn’t support language correction, or its related [`customWords`](vnrecognizetextrequest/customwords.md) array, for Chinese.

## See Also

- [Structuring Recognized Text on a Document](../visionkit/structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [Extracting phone numbers from text in images](extracting-phone-numbers-from-text-in-images.md)
  Analyze and filter phone numbers from text in live capture by using Vision.
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [class VNRecognizeTextRequest](vnrecognizetextrequest.md)
  An image-analysis request that finds and recognizes text in an image.
- [class VNRecognizedTextObservation](vnrecognizedtextobservation.md)
  A request that detects and recognizes regions of text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizing-text-in-images)*