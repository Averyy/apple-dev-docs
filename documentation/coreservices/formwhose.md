# formWhose

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var formWhose: Int { get }
```

#### Discussion

Specifies a container of one or more objects and a test to perform on the objects.

The key data for `formWhose` is specified by a whose descriptor, which is a coerced Apple event record of descriptor type `typeWhoseDescriptor`. The data for a whose descriptor consists of two keyword-specified descriptors with the keywords `keyAEIndex` and `keyAETest`.

See also the description for `formTest`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/formwhose)*