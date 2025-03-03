// format.js - Additional helper functions

/**
 * Format a date string into a human-readable format.
 * @param {string} dateStr - Date string in ISO format.
 * @returns {string} - Formatted date.
 */
export function formatDate(dateStr) {
  const date = new Date(dateStr);
  return date.toLocaleDateString();
}
