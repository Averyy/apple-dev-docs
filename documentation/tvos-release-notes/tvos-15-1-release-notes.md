# tvOS 15.1 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 15 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 15.1. The SDK comes bundled with Xcode 13, available from the Mac App Store. For information on the compatibility requirements for Xcode 13, see [`Xcode 13 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13-release-notes).

##### Coredata

###### Known Issues

- `NSExpression` immediately forbids certain operations that have significant side effects, like creating and destroying objects. Additionally, casting string class names into Class objects with `NSConstantValueExpression` is deprecated. (84017178)  Pass temporary objects to `NSExpression` in the context parameter of [`expressionValueWithObject:context:`](https://developer.apple.com/documentation/foundation/nsexpression/1410363-expressionvaluewithobject), or with `NSPredicate` as the `substitutionVariables` parameter of [`evaluateWithObject:substitutionVariables:`](https://developer.apple.com/documentation/foundation/nspredicate/1407759-evaluatewithobject). You can create a derived predicate with all the substitution variables replaced (bound), using [`withSubstitutionVariables(_:)`](https://developer.apple.com/documentation/foundation/nspredicate/1413227-withsubstitutionvariables) on an existing `NSPredicate` so that code using the object can continue to use a simple `evaluate(with object: Any?)` invocation.

## See Also

- [tvOS 15.6 Release Notes](tvos-15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.5 Release Notes](tvos-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.4 Release Notes](tvos-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.3 Release Notes](tvos-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.2 Release Notes](tvos-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15 Release Notes](tvos-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-15_1-release-notes)*