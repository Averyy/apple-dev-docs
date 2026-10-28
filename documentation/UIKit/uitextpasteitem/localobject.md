# localObject

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The custom local object that the copy or drag source optionally attached to the drag item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localObject: Any? { get }
```

```objc
@property (nonatomic, readonly, nullable) id localObject;
```

## Discussion

The local object is available only to the app that initiates the copy or drag activity.

## See Also

### Accessing the text paste item’s data
- [var itemProvider: NSItemProvider](./itemprovider.md)
  The item provider for the item being pasted or dropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpasteitem/localobject)*