/**
 * Generic API call function
 * @param {string} endpoint - API endpoint
 * @param {object} options - fetch options
 * @returns {Promise<any>} - Response data
 */
export async function fetchAPI(endpoint, options = {}) {
  const response = await fetch(`${process.env.API_BASE_URL}${endpoint}`, options);
  if (!response.ok) {
    throw new Error(`API error: ${response.statusText}`);
  }
  return await response.json();
}

/**
 * Example: Get crew list
 */
export function getCrewList() {
  return fetchAPI('/api/v1/crew/list');
}
