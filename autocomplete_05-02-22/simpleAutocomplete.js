let dict = ['apple', 'banana', 'cranberry', 'strawberry'];

function simpleAutocomplete(myString) {
    let matchArray = [];
    for (let i = 0; i < dict.length; i++) {
        if (dict[i].includes(myString)){
            matchArray.push(dict[i]);
        }
    }
    return matchArray;
}

module.exports = simpleAutocomplete;