# url(withAttributeString:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Constructs a URL given an attribute string.

**Availability**:
- macOS

## Declaration

```swift
func url(withAttributeString string: String!) -> URL!
```

```objc
- (NSURL *) URLWithAttributeString:(NSString *) string;
```

## Return Value

An `NSURL` object containing an absolute URL derived from the specified attribute string.

## Discussion

This method constructs a URL given the string value of an element attribute. Examples include the `href` attribute of a `DOMHTMLAnchorElement` object, or the `src` attribute of a `DOMHTMLImageElement` object. This method only applies to attributes that refer to URLs.

This method is similar to [`init(string:)`](../../Foundation/nsurl/init%28string%29.md) in the `NSURL` class, except that `URLWithAttributeString:` handles relative URLs automatically based on the current document’s location.

## Parameters

- `string`: The HTML attribute string to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domdocument/url(withattributestring:))*