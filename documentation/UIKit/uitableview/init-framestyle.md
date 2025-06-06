# init(frame:style:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a table view with the specified frame and style.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(frame: CGRect, style: UITableView.Style)
```

#### Return Value

Returns an initialized [`UITableView`](uitableview.md) object.

#### Discussion

You must specify the style of a table view when you create it, and you can’t change that style later. If you initialize the table view with the [`UIView`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html#//apple_ref/doc/uid/TP40007428-CH1-SW18) method [`init(frame:)`](uiview/init(frame:).md), the [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md) style is used as a default.

## Parameters

- `frame`: A rectangle specifying the initial location and size of the table view in its superview’s coordinates. The frame of the table view changes as table cells are added and deleted.
- `style`: A constant that specifies the style of the table view. For a list of valid styles, see  .

## See Also

- [init?(coder: NSCoder)](uitableview/init(coder:).md)
  Creates a table view object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/init(frame:style:))*