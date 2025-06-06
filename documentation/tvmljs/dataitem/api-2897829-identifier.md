# identifier

**Framework**: TVMLKit JS  
**Kind**: instp

A unique identifier for a data item provided by the associated JSON object.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
readonly attribute String identifier;
```

#### Discussion

The `identifier` property is mapped to the [`itemID`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/LanguagesUtilities/Conceptual/ATV_Template_Guide/TVJSAttributes.html#//apple_ref/doc/uid/TP40015064-CH42-SW1) attribute when the data item is converted to a DOM element. The underlying JSON objects being mapped must have a unique identifier for all JSON objects grouped under the same type.

## See Also

- [type](dataitem/2897825-type.md)
  The type for a data item provided by the associated JSON object. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/dataitem/2897829-identifier)*