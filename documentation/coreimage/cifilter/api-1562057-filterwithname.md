# filterWithName:keysAndValues:

**Framework**: Core Image  
**Kind**: clm

Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter and initializes the input values with a `nil`-terminated list of arguments.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
+ (CIFilter *)filterWithName:(NSString *)name keysAndValues:(id)key0, ...;
```

#### Return_value

A [`CIFilter`](cifilter.md) object whose input values are initialized.

#### Discussion

As with all Objective-C methods that accept `nil`-terminated argument lists, to prevent unintended behavior you must take take care not to pass a `nil` value before the intended end of the argument list. You can avoid such issues by using the [`filterWithName:withInputParameters:`](cifilter/1437894-filterwithname.md) method to create a filter, expressing the parameter list as a dictionary literal.

## Parameters

- `name`: The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method.
- `key0,...`: A list of key-value pairs to set as input values to the filter. Each key is a constant that specifies the name of the input value to set, and must be followed by a value. You signal the end of the list by passing a   value.

## See Also

- [+ filterWithName:](cifilter/1438255-filterwithname.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter. 
- [+ filterWithName:withInputParameters:](cifilter/1437894-filterwithname.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter and initializes the input values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1562057-filterwithname)*