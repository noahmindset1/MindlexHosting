// lambda_function.js
const { execSync } = require('child_process');

exports.handler = async (event, context) => {
    try {
        // Run Python bot
        const result = execSync('python3 bot.py');
        console.log(result.toString());
        
        return {
            statusCode: 200,
            body: JSON.stringify('Python bot executed successfully'),
        };
    } catch (error) {
        console.error(error);
        // Log error details to CloudWatch
        console.error(`Error executing Python bot: ${error.message}`);
        return {
            statusCode: 500,
            body: JSON.stringify('Error executing Python bot'),
        };
    }
};
