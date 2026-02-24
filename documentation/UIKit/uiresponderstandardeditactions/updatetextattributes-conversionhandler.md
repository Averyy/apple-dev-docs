# updateTextAttributes(conversionHandler:)

**Framework**: UIKit  
**Kind**: method

Tells your app to update the attributes of the currently selected text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func updateTextAttributes(conversionHandler: ([NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any])
```

#### Discussion

Implement this method if your app supports attributes that aren’t represented by other action methods such as [`toggleBoldface(_:)`](uiresponderstandardeditactions/toggleboldface(_:).md). The system calls this method to let responders know that the user or system applied new attributes for you to apply the current selection. In your implementation of this method, get the dictionary of the attributes associated with the selected content and pass it as a parameter to the `conversionHandler` block. When the block returns, apply the returned attributes to the selected text.

## Parameters

- `conversionHandler`: A handler block that you execute to retrieve the new attributes selected by the user. This block returns a dictionary containing the new values to apply to the text selection, and it takes the following parameter: - **attributes**: The dictionary of attributes that your app supports for the selected text. Specify all of the attributes and their current values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/updatetextattributes(conversionhandler:))*