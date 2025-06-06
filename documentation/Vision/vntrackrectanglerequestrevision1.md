# VNTrackRectangleRequestRevision1

**Framework**: Vision  
**Kind**: var

A constant for specifying revision 1 of the rectangling tracking request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
let VNTrackRectangleRequestRevision1: Int
```

#### Discussion

The revision number is a constant that you pass on a per-request basis to indicate to the Vision framework which version of the rectangle tracker to use for that request. Each OS release in which the framework improves aspects of the algorithm (recognition speed, accuracy, number of languages supported, and so forth), the revision number increments by 1.

By default, recognition requests use the latest—the highest—revision number for the SDK that your app links against. If you don’t recompile your app against a newer SDK, your app binary uses the revision that was the default at the time you last compiled it. If you do recompile, your app uses the default of the new SDK.

If your app must support users on older OS versions that don’t have access to the latest Vision framework, you may want to specify an earlier revision. For example, your algorithm may depend on specific behavior from a Vision request, such as writing your image processing algorithm to assume the size or aspect ratio of bounding boxes from an older revision of the face detector. In such a scenario, you can support earlier versions of the algorithm by specifying lower numbers:


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackrectanglerequestrevision1)*