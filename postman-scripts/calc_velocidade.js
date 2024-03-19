pm.test("Calcular velocidade retornou com sucesso", function () {
    pm.response.to.have.status(200);
});

pm.test("Velocidade é positiva", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.velocidade_metros_por_segundo).to.be.a('number');
    pm.expect(jsonData.velocidade_metros_por_segundo).to.be.above(0);
});