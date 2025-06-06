# url(withAttributeString:)

**Framework**: Webkit  
**Kind**: method

Constructs a URL given an attribute string.

**Availability**:
- macOS ?+

## Declaration

```swift
func url(withAttributeString string: String!) -> URL!
```

#### Return Value

An `NSURL` object containing an absolute URL derived from the specified attribute string.

#### Discussion

This method constructs a URL given the string value of an element attribute. Examples include the `href` attribute of a `DOMHTMLAnchorElement` object, or the `src` attribute of a `DOMHTMLImageElement` object. This method only applies to attributes that refer to URLs.

This method is similar to doc://com.apple.documentation/documentation/foundation/nsurl/1572047-urlwithstring in the `NSURL` class, except that `URLWithAttributeString:` handles relative URLs automatically based on the current document’s location.

## Parameters

- `string`: The HTML attribute string to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domdocument/url(withattributestring:))*