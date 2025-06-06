# watchOS 8.1 Release Notes

**Framework**: Watchos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 8 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 8.1. The SDK comes bundled with Xcode 13, available from the Mac App Store. For information on the compatibility requirements for Xcode 13, see [`Xcode 13 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13-release-notes).

##### Coredata

###### Known Issues

- `NSExpression` immediately forbids certain operations that have significant side effects, like creating and destroying objects. Additionally, casting string class names into Class objects with `NSConstantValueExpression` is deprecated. (84017178)  Pass temporary objects to `NSExpression` in the context parameter of [`expressionValueWithObject:context:`](https://developer.apple.com/documentation/foundation/nsexpression/1410363-expressionvaluewithobject), or with `NSPredicate` as the `substitutionVariables` parameter of [`evaluateWithObject:substitutionVariables:`](https://developer.apple.com/documentation/foundation/nspredicate/1407759-evaluatewithobject). You can create a derived predicate with all the substitution variables replaced (bound), using [`withSubstitutionVariables(_:)`](https://developer.apple.com/documentation/foundation/nspredicate/1413227-withsubstitutionvariables) on an existing `NSPredicate` so that code using the object can continue to use a simple `evaluate(with object: Any?)` invocation.

## See Also

- [watchOS 8.7 Release Notes](watchos-8_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.6 Release Notes](watchos-8_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.5 Release Notes](watchos-8_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.4 Release Notes](watchos-8_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.3 Release Notes](watchos-8_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8 Release Notes](watchos-8-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-8_1-release-notes)*