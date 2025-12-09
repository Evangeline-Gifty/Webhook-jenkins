post {
    success {
        emailext (
            to: 'evangelinegiftyy@gmail.com',
            subject: "SUCCESS: Job '${env.JOB_NAME}' #${env.BUILD_NUMBER}",
            body: """
<h2>Build Successful!!!!</h2>
<p>Job: ${env.JOB_NAME}</p>
<p>Build Number: ${env.BUILD_NUMBER}</p>
<p>Check details: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
""",
            mimeType: 'text/html'
        )
    }

    failure {
        emailext (
            to: 'evangelinegiftyy@gmail.com',
            subject: "FAILURE: Job '${env.JOB_NAME}' #${env.BUILD_NUMBER}",
            body: """
<h2>Build Failed!!!!</h2>
<p>Job: ${env.JOB_NAME}</p>
<p>Build Number: ${env.BUILD_NUMBER}</p>
<p>Check console log: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
""",
            mimeType: 'text/html'
        )
    }

    always {
        emailext(
            to: 'evangelinegiftyy@gmail.com',
            subject: "Job '${env.JOB_NAME}' #${env.BUILD_NUMBER} finished",
            body: "Check details: ${env.BUILD_URL}"
        )
    }
}
