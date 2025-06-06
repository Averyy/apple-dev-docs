# localizedDescription(forFilterName:)

**Framework**: Core Image  
**Kind**: clm

Returns the localized description of a filter for display in the user interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func localizedDescription(forFilterName filterName: String) -> String?
```

#### Return_value

The localized description of the filter.

## Parameters

- `filterName`: The filter name.

## See Also

- [class func localizedName(forFilterName: String) -> String?](cifilter/1437697-localizedname.md)
  Returns the localized name for the specified filter name.
- [class func localizedName(forCategory: String) -> String](cifilter/1438057-localizedname.md)
  Returns  the localized name for the specified filter category.
- [class func localizedReferenceDocumentation(forFilterName: String) -> URL?](cifilter/1437642-localizedreferencedocumentation.md)
  Returns the location of the localized reference documentation that describes the filter. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1437591-localizeddescription)*