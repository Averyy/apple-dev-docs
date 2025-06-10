# view(forUIConfiguration:excludedKeys:)

**Framework**: Core Image  
**Kind**: method

Returns a filter view for the filter.

**Availability**:
- macOS ?+

## Declaration

```swift
func view(forUIConfiguration inUIConfiguration: [AnyHashable : Any]!, excludedKeys inKeys: [Any]!) -> IKFilterUIView!
```

#### Return Value

An [`IKFilterUIView`](https://developer.apple.com/documentation/Quartz/IKFilterUIView) object.

#### Discussion

Calling this method to receive a view for a filter causes the [`CIFilter`](cifilter-swift.class.md) class to invoke the [`provideView(forUIConfiguration:excludedKeys:)`](https://developer.apple.com/documentation/Quartz/IKFilterCustomUIProvider/provideView(forUIConfiguration:excludedKeys:)) method. If you override [`provideView(forUIConfiguration:excludedKeys:)`](https://developer.apple.com/documentation/Quartz/IKFilterCustomUIProvider/provideView(forUIConfiguration:excludedKeys:)) the user interface is created by your filter subclass. Otherwise, Core Image automatically generates the user interface based on the filter keys and attributes.

Your app can retrieve a view whose control sizes complement the size of user interface elements already used in the application. It is also possible to choose which filter input parameters appear in the view. Consumer applications, for example, may want to show a small, basic set of input parameters whereas professional applications may want to provide access to all input parameters.

When you request a user interface for a parameter set, all keys for that set and below are included. For example, the advanced set consists of all parameters in the basic, intermediate and advanced sets. The development set should contain parameters that are either experimental or for debugging purposes. You should use them only during the development of filters and client applications, and not in a shipping product.

The controls in the view use bindings to set the values of the filter. See [`Cocoa Bindings Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i) if you are unfamiliar with bindings.

## Parameters

- `inUIConfiguration`: A dictionary that contains values for the   and   keys. For allowed values for the   key, see  . For allowed values for the   key, see  .
- `inKeys`: An array of the input keys for which you do   want to provide a user interface. Pass   if you want all input keys to be represented in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/view(foruiconfiguration:excludedkeys:))*