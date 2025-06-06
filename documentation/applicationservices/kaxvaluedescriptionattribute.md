# kAXValueDescriptionAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.5+

## Declaration

```swift
var kAXValueDescriptionAttribute: String { get }
```

#### Discussion

Used to supplement kAXValueAttribute. This attribute returns a string description that best describes the current value stored in kAXValueAttribute. This is useful for things like slider where the numeric value in kAXValueAttribute does not always convey enough information about the adjustment made on the slider. As an example, a color slider that adjusts thru various colors cannot be well-described by the numeric value in existing AXValueAttribute. This is where the kAXValueDescriptionAttribute comes in handy. In this example, the developer can provide the color information using this attribute.

Value: A localized, human-readable CFStringRef.

Writable? No.

Recommended for elements that support kAXValueAttribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxvaluedescriptionattribute)*