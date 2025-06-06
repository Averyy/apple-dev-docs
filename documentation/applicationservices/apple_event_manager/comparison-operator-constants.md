# Comparison Operator Constants

**Framework**: Application Services  
**Kind**: enum

Specify a comparison operation to perform on two operands.

#### Overview

When you call the [`CreateCompDescriptor(_:_:_:_:_:)`](https://developer.apple.com/documentation/coreservices/1449155-createcompdescriptor) function, you pass one of these comparison operators in the `comparisonOperator` parameter. The `CreateCompDescriptor` function creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.

The actual comparison of the two operands is performed by the object comparison function provided by the client application—see [`OSLCompareProcPtr`](https://developer.apple.com/documentation/coreservices/oslcompareprocptr). The way a comparison operator is interpreted is up to each application.

For related information, see [`Constants for Object Specifiers, Positions, and Logical and Comparison Operations`](https://developer.apple.com/documentation/coreservices/apple_events/1572744-constants_for_object_specifiers_). 

## Topics

### Constants
- [var kAEBeginsWith: OSType](../coreservices/kaebeginswith.md)
  The value of `operand1` begins with the value of `operand2` (for example, the string `"operand"` begins with the string `"opera"`).
- [var kAEContains: OSType](../coreservices/kaecontains.md)
  The value of `operand1` contains the value of `operand2 `(for example, the string `"operand"` contains the string `"era"`).
- [var kAECoreSuite: OSType](../coreservices/kaecoresuite.md)
  An Apple event in the Standard Suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/comparison_operator_constants)*