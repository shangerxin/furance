# Introduction
This is the test fixtures root folder. It is used to save the test materials for the web testing tools such as for testing TruClient, JMeter, UFT etc.

Each folder should be a subset of a test areas such as cross domain testing, common web elements, frameworks etc.


# How to add new cases
The test server will automatic organize the materials and generate a index for the web pages (*.html). If you want to self organize the test structure, please manually create a index.html in your subset folder. Then the test server will automatic add the index.html as reference for the subset folder.

- For a new subset suggest to create a new folder
- For a new cases suggest to create a new web page
- The subset folder can also contain any output of frameworks or webapp. Make sure the packaged output contain web pages or a index.html file.

