To create a CSS variable, you just need to give it a name with `two hyphens`(两个连词线) in front of it and assign it a value like this:


```html
<style>
    .test {
        --skin: gray;
    }
    .test-in {
        background: var(--skin, red);
    }
</style>
<body>
    <div class="test">
        <div class="test-in"> just try</div>
    </div>
</body>
```