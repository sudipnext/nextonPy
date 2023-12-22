const {fetch} = require('cross-fetch');
const {fs} = require('fs')

const url = 'https://graphql.anilist.co';
const perPage = 50; // Number of characters per page
let page = 1; // Initial page number
let hasNextPage = true; // Flag to determine if there are more pages

async function fetchCharacters() {
  const characters = [];

  while (hasNextPage) {
    const variables = {
      page: page,
      perPage: perPage,
    };

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        query: `
          query ($page: Int, $perPage: Int) {
            Page(page: $page, perPage: $perPage) {
              pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
              }
              characters {
                id
                name {
                  first
                  last
                }
                gender
                age
                media {
                  nodes {
                    title {
                      romaji
                    }
                  }
                }
              }
            }
          }
        `,
        variables: variables,
      }),
    };

    const response = await fetch(url, options);
    const { data, errors } = await response.json();

    if (errors) {
      console.error(errors);
      break; // Stop fetching in case of errors
    }

    const { Page } = data;
    const { pageInfo, characters: fetchedCharacters } = Page;

    // Process the fetched characters
    fetchedCharacters.forEach((character) => {
      const { name, gender, age, media } = character;
      const animeName = media.nodes.length > 0 ? media.nodes[0].title.romaji : null;

      characters.push({
        name: `${name.first} ${name.last}`,
        gender,
        age,
        animeName,
      });
    });

    hasNextPage = pageInfo.hasNextPage;
    page++;

    console.log(`Received data for page ${page - 1}`);
  }

  return characters;
}

async function saveCharactersToJson(characters) {
  const jsonData = JSON.stringify(characters, null, 2);

  fs.writeFile('characters.json', jsonData, (err) => {
    if (err) {
      console.error('Error saving characters to JSON:', err);
    } else {
      console.log('Characters saved to characters.json');
    }
  });
}

async function main() {
  try {
    const characters = await fetchCharacters();
    await saveCharactersToJson(characters);
  } catch (error) {
    console.error('Error retrieving characters:', error);
  }
}

main();
