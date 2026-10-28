# init(icon:text:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a search token with the specified text and icon (if any).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(icon: UIImage?, text: String)
```

```objc
+ (UISearchToken *) tokenWithIcon:(UIImage *) icon text:(NSString *) text;
```

## Return Value

A new search token.

## Parameters

- `icon`: An image to display with the text.
- `text`: The text to display on the search token.

## See Also

### Creating a search token
- [var representedObject: Any?](./representedobject.md)
  The object represented by the search token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtoken/init(icon:text:))*