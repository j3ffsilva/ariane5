pm.test("Get GPS for t1", function () {
    pm.response.to.have.status(200);
    var jsonData = pm.response.json();
    pm.collectionVariables.set("latitude_t1", jsonData.latitude);
    pm.collectionVariables.set("longitude_t1", jsonData.longitude);
});