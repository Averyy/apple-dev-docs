# value

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The raw value attribute of the element.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
var value: Any? { get }
```

```objc
@property (readonly, nullable) id value;
```

#### Discussion

The exact type of `value` varies based on the type of the element.

## See Also

### Value
- [var placeholderValue: String?](./placeholdervalue.md)
  The value displayed when the element has no value.
- [var title: String](./title.md)
  The title attribute of the element.
- [var label: String](./label.md)
  The label attribute of the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementattributes/value)*