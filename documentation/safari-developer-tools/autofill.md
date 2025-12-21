# Improving AutoFill experiences for your forms

**Framework**: Safari Developer Features

Use well-structured, standardized markup to enable a more reliable AutoFill experience for forms on your website.

#### Overview

AutoFill in Safari lets people automatically fill in credit card information, contact information, and credentials into forms on your webpages. With AutoFill, people can securely sign in to your website using credentials from their password manager, purchase products from your website quickly using payment information they previously saved, and accurately fill in shipping information to help make sure products ship to the correct address.

AutoFill works best when you use well-structured semantic markup to define the forms, inputs, and labels on your webpage. Safari uses multiple signals from your webpage to determine what information to offer people for filling in a particular input element. Even when customers don’t use AutoFill, these signals still help Safari provide a better user experience by offering tailored keyboards and input methods for different types of form controls.

#### Indicate the Purpose of Each Input

Safari considers the [`autocomplete`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete) attribute when determining how to fill a field. For example, add  `autocomplete="given-name"` and `autocomplete="family-name"` to the first and last name fields, respectively, to make it more likely that Safari offers to fill the customer’s first and last names into the fields. You can find valid values for the `autocomplete` attribute in the [`HTML Living Standard`](https://developer.apple.comhttps://html.spec.whatwg.org/dev/form-control-infrastructure.html#attr-fe-autocomplete).

> **Note**: Safari ignores `autocomplete="off"`, instead letting customers control the types of AutoFill that they enable from [`Safari Settings`](https://developer.apple.comhttps://support.apple.com/guide/safari/autofill-ibrwa005/18.0/mac/26.0).

Providing a value for the `autocomplete` attribute is particularly helpful for login flows where the purposes of form controls are otherwise difficult for AutoFill to detect, such as when form controls for login span multiple pages. To learn more about enabling Password AutoFill on  elements, see [`Enabling Password AutoFill on an HTML input element`](https://developer.apple.com/documentation/Security/enabling-password-autofill-on-an-html-input-element).

#### Associate Inputs with Their Labels

Both AutoFill and assistive technologies like VoiceOver benefit from a strong relationship between inputs and the text that labels them on your webpages. The [`<label>`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label) element provides an easy way to accomplish this for most input fields, allowing you to either nest the `<input>` inside the `<label>`, or add the `for` attribute to the label and set the value to the `id` attribute of the `<input>` it labels.

```html
<!-- An implicitly associated label -->
<label>
    First Name
    <input autocomplete="given-name" />
</label>

<!-- An explicitly associated label -->
<label for="first-name">First Name</label>
<input id="first-name" autocomplete="given-name" />
```

Alternatively, you can add the [`aria-labelledby`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby) attribute to any element and set it to the `id` of the element containing the text that labels the control.

```html
<!-- Assigning a label from the control itself -->
<label id="first-name-label">First Name</label>
<input aria-labelledby="first-name-label" autocomplete="given-name" />
```

Both approaches correctly associate the label text with the input and improve the accuracy of filling suggestions that Safari offers and the accessibility of your webpage for customers using VoiceOver. Prefer using `<label>` elements because they come with additional benefits, like allowing clicking or tapping on the `<label>` to interact with the `<input>`, which can make it easier to interact with controls like checkboxes by increasing the clickable area.

If you enable the [`Enabling features for web developers`](enabling-developer-features.md), you can use [`Web Inspector`](web-inspector.md) to inspect your form controls to confirm that you correctly associated labels with each control.

1. To open Web Inspector, Control-click on a form control and choose Inspect Element.
2. In the Elements tab, navigate to the [`Node details sidebar`](https://developer.apple.comhttps://webkit.org/web-inspector/elements-tab/#node-panel).
3. Find the Accessibility section.
4. Check the Label value and make sure it contains the text that labels the selected form control.

#### Use Form Elements to Group Logically Related Inputs

[`<form>`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form) elements help separate different forms on your pages. Even if you don’t use the built-in support `<form>` elements provide for submitting data and instead implement submission via JavaScript, using `<form>` elements can help separate different actions a customer can take. For example, for a page with separate login and new account forms, use two different `<form>` elements — one for each form. Similarly, place any other forms on the page, like a search form, in their own `<form>`.

#### Validate Controls Using Built in Validation Instead of Custom Javascript

HTML provides numerous ways to configure form controls to ensure they accept only expected values without using JavaScript. This allows WebKit to enforce common validation rules on your behalf, and allows Safari to offer relevant AutoFill suggestions that are appropriate for your form controls. Attributes like `type`, `minlength`, `maxlength`, and `pattern` let you limit the number and type of characters in the control. To learn more about form validation, see [`Using HTML form validation and the Constraint Validation API`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation).

The [`type`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#input_types) attribute allows browsers to provide helpful input methods for different types of information, like presenting a keypad tailored to entering a phone number in iOS when using the `tel` value, or obscuring the typed value when using the `password` value. Form validation takes some `type` values into account, like `email`, to help ensure people don’t submit forms with an improperly formatted email address.

The [`pattern`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern) attribute is particularly useful because it allows you to limit the types of characters the control accepts as valid. For example, a credit card number control could specify a pattern like `[0-9]` to ensure only digits are valid.

> ❗ **Important**: Avoid using the `pattern` attribute to enforce restrictions like only using the Latin alphabet or forcing customers to enter phone numbers with dashes between groups of numbers, because these conventions can vary across the world. When possible, be flexible with input validation in situations where you can correctly format the information yourself afterward, like a phone number where you allow both hyphenated and nonhyphenated entry, and strip nonnumeric characters after submission.

The `passwordrules` attribute allows Safari to suggest an appropriate strong password if your webpage has uncommon restrictions on passwords, which may exist to remain compatible with other technologies. Because character limitations in passwords may frustrate customers trying to create an account, accept a wide variety of special characters whenever possible on your website. When necessary, the `passwordrules` attribute lets you be specific about requirements like requiring at least one uppercase character, lowercase character, and digit. To learn more about customizing Password AutoFill rules, see [`Customizing Password AutoFill rules`](https://developer.apple.com/documentation/Security/customizing-password-autofill-rules).

> **Note**: To help ensure that AutoFill works seamlessly across the web, Apple archives copies of live webpages. Apple uses the layout and structure of the archived pages to evaluate and improve the AutoFill experience. For pages that require an account for access, accounts are manually created and logged in to for the purpose of archiving forms. Websites can prevent this manual archiving of pages behind login by blocking account creation or preventing login for accounts with usernames and email address names ending with `safariautofill`. For example, an email address matching this format could be `testaccountsafariautofill@example.com`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/autofill)*