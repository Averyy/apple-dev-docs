# printContent(_:)

**Framework**: UIKit  
**Kind**: method

Tells your app to print available content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printContent(_ sender: Any?)
```

#### Discussion

Implement this method on the responder responsible for printing the contents of the window scene; for instance, the root view controller of a [`UIWindow`](uiwindow.md). In your implementation, prepare the print job and present an instance of [`UIPrintInteractionController`](uiprintinteractioncontroller.md) to show a Print dialog.

If your app includes the [`UIApplicationSupportsPrintCommand`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSupportsPrintCommand) key in its `Info.plist` file, people can print from your app using the keyboard shortcut Command-P, which calls [`printContent(_:)`](uiresponderstandardeditactions/printcontent(_:).md). You can also set [`printContent(_:)`](uiresponderstandardeditactions/printcontent(_:).md) as the action on other print-related controls such as a print button on a toolbar.

For more information about printing from your app, see [`Printing`](printing.md).

## Parameters

- `sender`: The object calling this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/printcontent(_:))*