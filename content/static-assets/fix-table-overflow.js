/**
 * Short little bit of JS to add overflow: scroll to any table that represents a
 * dataframe. In general, these tables tend to be very wide and bleed off of the
 * page.
 */

const dataFrameTables = document.querySelectorAll('table.dataframe')
for (const table of dataFrameTables) {
    const parentDiv = table.parentElement
    parentDiv.style.overflow = 'scroll'
}
