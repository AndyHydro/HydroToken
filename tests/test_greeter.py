# def test_greeter(chain):
#     greeter, _ = chain.provider.get_or_deploy_contract('Greeter')
#
#     greeting = greeter.call().greet()
#     assert greeting == 'Hello'
#
#
# def test_custom_greeting(chain):
#     greeter, _ = chain.provider.get_or_deploy_contract('Greeter')
#
#     set_txn_hash = greeter.transact().setGreeting('Guten Tag')
#     chain.wait.for_receipt(set_txn_hash)
#
#     greeting = greeter.call().greet()
#     assert greeting == 'Guten Tag'
def test_hydro(web3, chain):
    hydro, _ = chain.provider.get_or_deploy_contract('HydroTokenV2')

    address = web3.eth.coinbase

    # whitelist(address, hydro, web3, chain)
    #
    # hydroPartnerMap(address, hydro, web3, chain)
    #
    # authenticate(address, hydro, web3, chain)
    #
    # authenticated = hydro.call().validateAuthentication(address, 1, 1)
    # assert authenticated == True
    #
    # authenticated = hydro.call().validateAuthentication(address, 2, 1)
    # assert authenticated == False
    #
    # authenticated = hydro.call().validateAuthentication(address, 1, 2)
    # assert authenticated == False
