---
description: Kick off your Vale journey by building a rule that nudges writers to focus on user tasks over UI labels.
---

# Creating Your First Vale Rule for Documentation
Vale helps enforce writing style in documentation, ensuring clarity and consistency. In this tutorial, you'll create your first custom rule: one that encourages writers to shift from UI-heavy phrasing to user-focused instructions.

---

## Create the Vale Configuration File
Vale looks for a `.vale.ini` file to know which styles to apply. After installing Vale, you'll need to create this file in your working directory. Add the following basic configuration to the `.vale.ini` file and save it:

```ini
StylesPath = styles

[*]
BasedOnStyles = CustomRules
```

- `StylesPath = styles` defines the directory where Vale looks for style rule definitions.
- `[*]` applies rules to all file types by default. If you want different rules for Markdown or AsciiDoc, you can specify them under `[md]` or `[adoc]`.
- `BasedOnStyles = CustomRules` tells Vale to use the `CustomRules` style guide, and you'll create a *CustomRules* directory inside the *styles* directory to store your custom checks.

## Create the Styles Directory
<span class="step-number">1</span> Create a *styles* directory inside your working directory. 

<span class="step-number">2</span> Inside the *styles* directory, create the *CustomRules* directory.

![Creating folders for vale](valebasic1.png)

## Create the CustomRules File
Now that you've set up the *CustomRules* directory, it's time to define a custom style rule.

Create a new file named `CustomRules.yml` in the *CustomRules* directory.

To ensure documentation focuses on what the user needs to do, rather than how they interact with the UI, let's define YML rules to flag UI elements. Add the following rules to the `CustomRules.yml` file:

```yml
extends: existence
message: "Avoid referring to UI elements directly."
level: warning
nonword: true
tokens:
  - "checkbox"
  - "check box"
  - "radio button"
  - "button"
```

## Test Vale Against a Sample File
<span class="step-number">1</span> Create a sample file (for example, `sample.txt`) in the working directory.

<span class="step-number">2</span> Add some sentences with UI elements to the sample file: 

```text
Click the button to submit.
Select the checkbox to enable dark mode.
```

<span class="step-number">3</span> Run Vale to check the file:

`vale sample.txt`

When you run the command, Vale will alert you that two sentences contain UI-related terms:

![Vale warning that sentences contain UI terms](valebasic2.png)

## Fix Sentences Flagged by Vale  

The writer can revise sentences as follows to ensure UI elements are not explicitly mentioned:  

| Original Sentence (Flagged by Vale) | Revised Sentence |
|-------------------------------------|------------------|
| Click the button to submit.        | Submit the form. |
| Select the checkbox to enable dark mode. | Enable dark mode in settings. |

Congratulations! You've successfully set up your first YML rule for Vale. Taking advantage of Vale is a great way to improve documentation quality and ensure consistency.