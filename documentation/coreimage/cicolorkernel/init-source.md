# init(source:)

**Framework**: Core Image  
**Kind**: init

Creates a color kernel object from the specified kernel source code.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init?(source string: String)
```

#### Return Value

A new color kernel object, or `nil` if the specified source code does not contain a valid color kernel routine.

#### Discussion

This method is similar to the [`init(source:)`](cikernel/init(source:).md) method of the superclass [`CIKernel`](cikernel.md), but creates only color kernels. Use this method when you want to ensure that the type of kernel object returned (if any) is always [`CIColorKernel`](cicolorkernel.md).

## Parameters

- `string`: A program in the Core Image Kernel Language that contains a single routine marked using the   keyword.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorkernel/init(source:))*