# formTest

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var formTest: Int { get }
```

#### Discussion

Specifies a test. The key data is specified by either a comparison descriptor or a logical descriptor.

The Apple Event Manager internally translates object specifiers of key form `formTest` into object specifiers of key form `formWhose` to optimize resolution of object specifiers. This involves collapsing the key form and key data from two object specifiers in a container hierarchy into one object specifier with the key form `formWhose`.

See also [`AEDisposeToken(_:)`](1446783-aedisposetoken.md), [`Constants for Object Specifiers, Positions, and Logical and Comparison Operations`](apple_events/1572744-constants_for_object_specifiers_.md), [`CreateCompDescriptor(_:_:_:_:_:)`](1449155-createcompdescriptor.md), and [`CreateLogicalDescriptor(_:_:_:_:)`](1445212-createlogicaldescriptor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/formtest)*