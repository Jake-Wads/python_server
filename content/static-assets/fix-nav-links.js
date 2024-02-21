/** 
 * For some reason, the navigation links at the bottom of the page are broken.
 * They try to link to the next and previous pages by appending to the url,
 * instead of replacing. For example, if we are on lesson 1, the generated
 * "next" link will be:
 * 
 *      /lesson-1/lesson-2
 * 
 * But we really want it to be:
 * 
 *      /lesson-2
 */

const last = s => s[s.length - 1]

const links = {
    prev: document.querySelector('a[rel=prev]'),
    next: document.querySelector('a[rel=next]'),
}

const realPreviousLink = last(links.prev.href.replace(/\/$/, '').split('/'))
const realNextLink = last(links.next.href.replace(/\/$/, '').split('/'))

console.log(`replacing ${links.prev.href} with ${realPreviousLink}`);
console.log(`replacing ${links.next.href} with ${realNextLink}`);


links.prev.href = `/${realPreviousLink}`
links.next.href = `/${realNextLink}`