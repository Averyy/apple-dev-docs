# registerName(_:constructor:classAttributes:)

**Framework**: Core Image  
**Kind**: clm

Publishes a custom filter that is not packaged as an image unit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func registerName(_ name: String, constructor anObject: any CIFilterConstructor, classAttributes attributes: [String : Any] = [:])
```

#### Discussion

In most cases you don’t need to use this method because the preferred way to register a custom filter that you write is to package it as an image unit. You do not need to use this method for a filter packaged as an image unit because you  register your filter using the `CIPlugInRegistration` protocol. (See [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for additional details.)

## Parameters

- `name`: A string object that specifies the name of the filter you want to publish.
- `anObject`: A constructor object that implements the   method. 
- `attributes`: A dictionary that contains the class display name and filter categories attributes along with the appropriate value for each attributes. That is,  the   attribute and a string that specifies the display name, and the   and an array that specifies the categories to which the filter belongs (such as   and  ). All other attributes for the filter should be returned by the custom   method implement by the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1437889-registername)*