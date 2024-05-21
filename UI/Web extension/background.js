chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'getTabUrl') {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            const currentTab = tabs[0];
            sendResponse({ url: currentTab.url });
        });
        return true;  // Indică faptul că răspunsul va fi trimis asincron
    }
});
