const simpleAutocomplete = require('./simpleAutocomplete');

test ('app matches 1 result', () => {
    expect(simpleAutocomplete('app')).toStrictEqual(['apple']);
});

test ('berry matches 2 results', () => {
    expect(simpleAutocomplete('berry')).toStrictEqual(['cranberry', 'strawberry']);
});

test ('Berry matches 0 results', () => {
    expect(simpleAutocomplete('Berry')).toStrictEqual([]);
});

test ('fact matches 0 results', () => {
    expect(simpleAutocomplete('fact')).toStrictEqual([]);
});