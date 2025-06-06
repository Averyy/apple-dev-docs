# videoEditorController(_:didFailWithError:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when the video editor is unable to load or save a movie.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func videoEditorController(_ editor: UIVideoEditorController, didFailWithError error: any Error)
```

#### Discussion

Loading a movie into the video editor could fail because of an invalid filesystem path or an invalid media format. Saving could fail because of a lack of disk space or other reasons.

## Parameters

- `editor`: The video editor that was unable to load or save a movie.
- `error`: The loading or saving error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didfailwitherror:))*