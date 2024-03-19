pm.test("Get GPS for t0", function () {
    pm.response.to.have.status(200);
    var jsonData = pm.response.json();
    pm.collectionVariables.set("latitude_t0", jsonData.latitude);
    pm.collectionVariables.set("longitude_t0", jsonData.longitude);
});