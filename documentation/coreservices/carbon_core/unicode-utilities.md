# Unicode Utilities

**Framework**: Core Services

Work with Unicode text.

## Topics

### Inputting Unicode Text
- [func UCKeyTranslate(UnsafePointer<UCKeyboardLayout>!, UInt16, UInt16, UInt32, UInt32, OptionBits, UnsafeMutablePointer<UInt32>!, Int, UnsafeMutablePointer<Int>!, UnsafeMutablePointer<UniChar>!) -> OSStatus](1390584-uckeytranslate.md)
  Converts a combination of a virtual key code, a modifier key state, and a dead-key state into a string of one or more Unicode characters.
### Comparing Unicode Strings
- [func UCCreateCollator(LocaleRef!, LocaleOperationVariant, UCCollateOptions, UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390403-uccreatecollator.md)
  Creates an object encapsulating locale and collation information, for the purpose of performing Unicode string comparison.
- [func UCCompareText(CollatorRef!, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390642-uccomparetext.md)
  Uses locale-specific collation information to compare Unicode strings.
- [func UCGetCollationKey(CollatorRef!, UnsafePointer<UniChar>!, Int, Int, UnsafeMutablePointer<Int>!, UnsafeMutablePointer<UCCollationValue>!) -> OSStatus](1390468-ucgetcollationkey.md)
  Uses locale-specific collation information to generate a collation key for a Unicode string.
- [func UCCompareCollationKeys(UnsafePointer<UCCollationValue>!, Int, UnsafePointer<UCCollationValue>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390378-uccomparecollationkeys.md)
  Uses collation keys to compare Unicode strings.
- [func UCDisposeCollator(UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390435-ucdisposecollator.md)
  Disposes a collator object.
- [func UCCompareTextDefault(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390472-uccomparetextdefault.md)
  Uses the default system locale to compare Unicode strings.
- [func UCCompareTextNoLocale(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390513-uccomparetextnolocale.md)
  Uses a fixed, locale-insensitive order to compare Unicode strings.
### Data Types
- [typealias CollatorRef](collatorref.md)
  Refers to an opaque object that encapsulates locale and collation information for the purpose of performing Unicode string comparison.
- [typealias TextBreakLocatorRef](textbreaklocatorref.md)
  Refers to an opaque object that encapsulates locale and text-break information for the purpose of finding boundaries in Unicode text.
- [typealias UCCollationValue](uccollationvalue.md)
  Specifies a Unicode collation key.
- [struct UCKeyboardLayout](uckeyboardlayout.md)
  Provides header data for a `'uchr'` resource.
- [struct UCKeyboardTypeHeader](uckeyboardtypeheader.md)
  Specifies a range of physical keyboard types in a `'uchr'` resource. 
- [typealias UCKeyCharSeq](uckeycharseq.md)
  Specifies the output of a dead-key state in a `'uchr'` resource.
- [struct UCKeyLayoutFeatureInfo](uckeylayoutfeatureinfo.md)
  Specifies the longest possible output string to be produced by the current `'uchr'` resource.
- [struct UCKeyModifiersToTableNum](uckeymodifierstotablenum.md)
  Maps a modifier key combination to a particular key-code-to-character table number in a `'uchr'` resource.
- [typealias UCKeyOutput](uckeyoutput.md)
  Specifies values in key-code-to-character tables in a `'uchr'` resource.
- [struct UCKeySequenceDataIndex](uckeysequencedataindex.md)
  Contains offsets to a list of character sequences for a `'uchr'` resource.
- [struct UCKeyStateEntryRange](uckeystateentryrange.md)
  Maps from a dead-key state to either the resultant Unicode character(s) or the new dead key state produced when the current state is terminated by a given character key for a `'uchr'` resource.
- [struct UCKeyStateEntryTerminal](uckeystateentryterminal.md)
  Maps from a dead-key state to the Unicode character(s) produced when that state is terminated by a given character key for a `'uchr'` resource.
- [struct UCKeyStateRecord](uckeystaterecord.md)
  Determines dead-key state transitions in a `'uchr'` resource.
- [struct UCKeyStateRecordsIndex](uckeystaterecordsindex.md)
  Provides a count of, and offsets to, dead-key state records in a `'uchr'` resource.
- [struct UCKeyStateTerminators](uckeystateterminators.md)
  Lists the default terminators for each dead-key state handled by a `'uchr'` resource.
- [struct UCKeyToCharTableIndex](uckeytochartableindex.md)
  Provides a count of, and offsets to, key-code-to-character tables in a `'uchr'` resource.
### Constants
- [Fixed Ordering Scheme](carbon_core/unicode_utilities/1390361-fixed_ordering_scheme.md)
  Specifies to use the fixed ordering scheme.
- [Fixed Ordering Masks 1](carbon_core/unicode_utilities/1390370-fixed_ordering_masks_1.md)
  Set and test the `UCCollateOptions` field that specifies a fixed ordering scheme.
- [Fixed Ordering Masks 2](carbon_core/unicode_utilities/1390573-fixed_ordering_masks_2.md)
  Test the `UCCollateOptions` field that specifies a fixed ordering scheme.
- [Key Actions](carbon_core/unicode_utilities/1390619-key_actions.md)
  Indicate the current key action.
- [Key Format Codes](carbon_core/unicode_utilities/1390609-key_format_codes.md)
  Indicate a structure format used in a `'uchr'` resource.
- [Key Output Index Masks](carbon_core/unicode_utilities/1390638-key_output_index_masks.md)
  Test the bits in `UCKeyOutput` values.
- [Key State Entry Formats](carbon_core/unicode_utilities/1390376-key_state_entry_formats.md)
  Indicate the format for dead-key state records.
- [Key Translation Options Flag](carbon_core/unicode_utilities/1390507-key_translation_options_flag.md)
  Indicates the dead-key processing state.
- [Key Translation Options Mask](carbon_core/unicode_utilities/1390568-key_translation_options_mask.md)
  Specifies the mask for the bit that controls dead-key processing state.
- [Operation Class](carbon_core/unicode_utilities/1390359-operation_class.md)
  Identifies collation as a class of Unicode utility operations.
- [Standard Options Mask](carbon_core/unicode_utilities/1390444-standard_options_mask.md)
  Specifies standard options for Unicode string comparison.
- [typealias UCCollateOptions](uccollateoptions.md)
  Specifies options for Unicode string comparison.
- [typealias UCTextBreakOptions](uctextbreakoptions.md)
  Specifies options for locating boundaries in Unicode text.
- [typealias UCTextBreakType](uctextbreaktype.md)
  Specifies kinds of text boundaries.
- [Text Boundary Operation Class](carbon_core/unicode_utilities/1390460-text_boundary_operation_class.md)
  Identifies the class of Unicode utility operations that find text boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/unicode_utilities)*