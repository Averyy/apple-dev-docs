# Choice

**Framework**: Installer JS  
**Kind**: uid

A single installation choice. 

#### Overview

Choice objects are properties of the `choices` global variable and represent the installation choices defined in a distribution package.

The name of each property of the `choices` array corresponds to the `choice-id` attribute of each of the distribution’s installation choices (see [`Distribution Definition XML Schema Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Introduction.html#//apple_ref/doc/uid/TP40005370) for more information). Therefore, a specific choice is accessed this way:

```javascript
choices.<choice-id>
```

`<choice-id>` represents the identifier of the desired choice in the installation definition. For example, to access the `selected` property of a choice with `'choice_a'` as its identifier, you would use the following expression:

```javascript
choices.['choice_a'].selected
```

## Topics

### Accessing a Choice’s State
- [selected](choice/1812159-selected.md)
  A Boolean value that indicates whether the choice is selected.
- [enabled](choice/1812168-enabled.md)
  A Boolean value that indicates whether the choice is enabled.
- [visible](choice/1812175-visible.md)
  A Boolean that indicates whether the choice is visible.
### Accessing a Choice’s Metadata
- [title](choice/1812183-title.md)
  The title of the distribution package, as a String.
- [description](choice/1812191-description.md)
  The description of the distribution, as a String.
### Working with Packages
- [packages](choice/1812201-packages.md)
  An array identifying each package attached to the choice.
- [packageUpgradeAction](choice/1812213-packageupgradeaction.md)
  A string specifying the relationship between the choice’s packages (specified by the packages property) and the same packages (based on the package identifier) installed on the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/choice)*