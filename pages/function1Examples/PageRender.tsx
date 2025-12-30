
    import { ElementRender } from 'jit-widgets';
    import { pageStyle , pageGlobalStyle } from './page.style'
    export default (props) => {
    
        return (
            <ElementRender
                pageStyle={pageStyle}
                pageGlobalStyle={pageGlobalStyle}
                {...props}
                elementPath="pages.GridPageType"
            />
        );
    };
                