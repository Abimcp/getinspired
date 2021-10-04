import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';

import { inspirationReducer } from './reducers';

const store = createStore(inspirationReducer, composeWithDevTools(applyMiddleware(thunk)));

export default store;