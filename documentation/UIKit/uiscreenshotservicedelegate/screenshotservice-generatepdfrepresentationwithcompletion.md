# screenshotService(_:generatePDFRepresentationWithCompletion:)

**Framework**: UIKit  
**Kind**: method

Generates a high-fidelity PDF version of the entire content in a given window scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+

## Declaration

```swift
@MainActor
optional func screenshotServiceGeneratePDFRepresentation(_ screenshotService: UIScreenshotService) async -> (Data?, Int, CGRect)
```

#### Discussion

When the user takes a screenshot of your app, UIKit calls this method to ask you for a PDF version of your content. In your implementation, create a high-fidelity PDF version of your content. At the end of your method, call `completionHandler` with the results.

## Parameters

- `screenshotService`: A screenshot service object assigned to the relevant   object. Use the window scene to retrieve the windows of your interface, and generate the PDF content from those windows.
- `completionHandler`: Specify   if you cannot provide the visible rectangle, or if you want the system to always display the PDF content starting at the top of the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreenshotservicedelegate/screenshotservice(_:generatepdfrepresentationwithcompletion:))*