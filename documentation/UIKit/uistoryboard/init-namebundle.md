# init(name:bundle:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a storyboard object for the specified resource file.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(name: String, bundle storyboardBundleOrNil: Bundle?)
```

#### Return Value

A storyboard object for the specified file. If no storyboard resource file matching `name` exists, an exception is thrown with description: `Could not find a storyboard named 'XXXXXX' in bundle...`.

#### Discussion

Use this method to retrieve the storyboard object containing the view controller graph you want to access. All of the resources associated with the storyboard must be in the bundle indicated by the `storyboardBundleOrNil` parameter.

## Parameters

- `name`: The name of the storyboard resource file without the filename extension. This method raises an exception if this parameter is  .
- `storyboardBundleOrNil`: The bundle containing the storyboard file and its related resources. If you specify  , this method looks in the main bundle of the current application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard/init(name:bundle:))*